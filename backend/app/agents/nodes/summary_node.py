def summary_node(

    state

):

    state["summary"] = (

        f"Risk Score: "

        f"{state['risk_score']}"

    )


    return state