class AggregatorAgent:
    """
    Combines results from all AI agents and produces final structured review.
    """

    def aggregate(self, bug_result, security_result, performance_result, style_result):

        # -----------------------------
        # SAFE NORMALIZATION
        # -----------------------------
        bugs = bug_result if isinstance(bug_result, list) else bug_result.get("bugs", [])
        security = security_result if isinstance(security_result, list) else security_result.get("security", [])
        performance = performance_result if isinstance(performance_result, list) else performance_result.get("performance", [])
        style = style_result if isinstance(style_result, list) else style_result.get("style", [])

        # -----------------------------
        # RISK SCORE
        # -----------------------------
        risk_score = self._calculate_risk(bugs, security, performance, style)

        # -----------------------------
        # DECISION LOGIC
        # -----------------------------
        if risk_score <= 20:
            decision = "APPROVE"
        elif risk_score <= 50:
            decision = "MINOR_FIXES"
        elif risk_score <= 80:
            decision = "REQUEST_CHANGES"
        else:
            decision = "BLOCK_MERGE"

        # -----------------------------
        # FINAL RESPONSE (IMPORTANT)
        # -----------------------------
        return {
            "status": "success",

            "summary": {
                "total_bugs": len(bugs),
                "total_security_issues": len(security),
                "total_performance_issues": len(performance),
                "total_style_issues": len(style),
                "total_issues": len(bugs) + len(security) + len(performance) + len(style)
            },

            "review": {
                "bugs": bugs,
                "security": security,
                "performance": performance,
                "style": style
            },

            "analysis": {
                "risk_score": risk_score,
                "decision": decision
            }
        }

    def _calculate_risk(self, bugs, security, performance, style):

        total = 0

        if isinstance(bugs, list):
            total += len(bugs) * 3

        if isinstance(security, list):
            total += len(security) * 5

        if isinstance(performance, list):
            total += len(performance) * 2

        if isinstance(style, list):
            total += len(style) * 1

        return min(total, 100)