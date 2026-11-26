import json
import re
from typing import Any, Dict, Optional

class ExplainAnalyzer:
    def __init__(self, cost_threshold: float = 1000.0):
        self.cost_threshold = cost_threshold

    def analyze_plan(self, explain_output: str) -> Dict[str, Any]:
        """
        Parses EXPLAIN output (JSON format for PostgreSQL) and extracts metrics.
        """
        try:
            plan_data = json.loads(explain_output)
            if isinstance(plan_data, list):
                plan_data = plan_data[0].get("Plan", {})
            else:
                plan_data = plan_data.get("Plan", {})

            metrics = {
                "total_cost": plan_data.get("Total Cost", 0.0),
                "rows": plan_data.get("Plan Rows", 0),
                "is_full_scan": self._detect_full_scan(plan_data),
                "depth": self._calculate_depth(plan_data)
            }
            return metrics
        except (json.JSONDecodeError, AttributeError):
            return {"error": "Invalid EXPLAIN format"}

    def _detect_full_scan(self, plan: Dict[str, Any]) -> bool:
        node_type = plan.get("Node Type", "")
        if node_type == "Seq Scan":
            return True
        for child in plan.get("Plans", []):
            if self._detect_full_scan(child):
                return True
        return False

    def _calculate_depth(self, plan: Dict[str, Any]) -> int:
        children = plan.get("Plans", [])
        if not children:
            return 1
        return 1 + max(self._calculate_depth(c) for c in children)

    def is_query_safe(self, explain_output: str) -> bool:
        metrics = self.analyze_plan(explain_output)
        if "error" in metrics:
            return False
        if metrics["total_cost"] > self.cost_threshold:
            return False
        if metrics["is_full_scan"] and metrics["rows"] > 10000:
            return False
        return True