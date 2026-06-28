def risk_node(

    state

):

    total = (

        len(

            state["security_issues"]

        )

        +

        len(

            state["bug_issues"]

        )

        +

        len(

            state["performance_issues"]

        )

        +

        len(

            state["style_issues"]

        )

    )


    state["risk_score"] = total * 10


    return state