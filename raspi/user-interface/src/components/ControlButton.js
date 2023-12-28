import { ACTIONS } from "../App";
import "./ControlButton.css";

export default function ControlButton({dispatch, label}) {
    // needs to update status bar on click
    return (
        <button className="control-button">
            {label}
        </button>
    )
}
