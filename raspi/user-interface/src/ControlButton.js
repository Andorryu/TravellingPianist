import { ACTIONS } from "./App";

export default function ControlButton({dispatch, label}) {
    // needs to update status bar on click
    return (
        <button>
            {label}
        </button>
    )
}