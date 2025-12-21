import { useState } from "react";

function IngredientList({ items, onRemove, onEdit }) {

    const [editingID, setEditingID] = useState(null)
    const [draftValue, setDraftValue] = useState("")

    function startEdit(item) {
        setEditingID(item.id)
        setDraftValue(item.name)

    }

    function cancelEdit() {
        setEditingID(null)
        setDraftValue("")
    }

    function saveEdit() {
        const cleaned = draftValue.trim()
        if(cleaned === "") return

        onEdit(cleaned, editingID)
        setEditingID(null)
        setDraftValue("")

    }

    return (
        <>

            <ul>
                {items.map((item) => {
                    if(item.id === editingID) {
                        return (
                            <list key= {item.id}>
                                <input
                                    value = {draftValue}
                                    onChange = {(e) => setDraftValue(e.target.value)}
                                />
                                <button onClick = {saveEdit}> Save </button>
                                <button onClick = {cancelEdit}> Cancel</button>
                            </list>
                        )                        

                        
                    }

                    return(
                    <li key={item.id}> {item.name}
                        
                        <button onClick={() => startEdit(item)}>Edit</button>
                        <button onClick={() => onRemove(item.id)}>remove</button>
                    </li>
                    )

                })}
            </ul>
        </>
    )

}
export default IngredientList