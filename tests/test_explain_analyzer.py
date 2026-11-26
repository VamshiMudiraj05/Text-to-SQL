import pytest
from src.security.explain_analyzer import ExplainAnalyzer

def test_analyze_plan_cost_threshold():
    analyzer = ExplainAnalyzer(cost_threshold=500.0)
    
    safe_plan = json.dumps([{"Plan": {"Total Cost": 100.0, "Plan Rows": 10, "Node Type": "Index Scan"}}])
    unsafe_plan = json.dumps([{"Plan": {"Total Cost": 1000.0, "Plan Rows": 1000, "Node Type": "Seq Scan"}}])
    
    assert analyzer.is_query_safe(safe_plan) is True
    assert analyzer.is_query_safe(unsafe_plan) is False

def test_detect_full_scan():
    analyzer = ExplainAnalyzer()
    full_scan_plan = json.dumps([{"Plan": {"Node Type": "Seq Scan", "Total Cost": 10.0, "Plan Rows": 20000}}])
    
    # Should be unsafe due to full scan + high rows
    assert analyzer.is_query_safe(full_scan_plan) is False

def test_nested_plan_depth():
    analyzer = ExplainAnalyzer()
    plan = {
        "Plan": {
            "Node Type": "Hash Join",
            "Plans": [
                {"Node Type": "Seq Scan"},
                {"Node Type": "Index Scan", "Plans": [{"Node Type": "Bitmap Heap Scan"}]}
            ]
        }
    }
    metrics = analyzer.analyze_plan(json.dumps(plan))
    assert metrics["depth"] == 3

import json