def decision_node(

    state

):

    score = state["risk_score"]


    if score < 30:

        decision = "APPROVE"

    elif score < 60:

        decision = "COMMENT"

    else:

        decision = "REQUEST_CHANGES"


    state["decision"] = decision


    return state