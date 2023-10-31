from state import CurrentStep
import streamlit as st


def set_form_step(action, step=None):
    """Maintains the user's location within the wizard."""
    if action == "Jump" and step is not None:
        st.session_state[CurrentStep] = step


def render_side_buttons():
    with st.sidebar:
        def button_type(i: int) -> str:
            """Determines button color: red when user is on that given step."""
            return "primary" if st.session_state[CurrentStep] == i else "secondary"

        st.button(
            "Metadata",
            on_click=set_form_step,
            args=["Jump", "metadata"],
            type=button_type("metadata"),
            use_container_width=True,
        )
        st.button(
            "Files",
            on_click=set_form_step,
            args=["Jump", "files"],
            type=button_type("files"),
            use_container_width=True,
        )
        st.button(
            "RecordSets",
            on_click=set_form_step,
            args=["Jump", 3],
            type=button_type("recordsets"),
            use_container_width=True,
        )