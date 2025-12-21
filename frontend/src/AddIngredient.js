import { useState } from "react";

function AddIngredient({ onAdd }) {
    const [newItem, setNewItem] = useState("")

    function handleAdd() {
        onAdd(newItem)
        setNewItem("")
    }

    return (
        <>
            <input
                placeholder="New Ingredient"
                value={newItem}
                onChange={(e) => setNewItem(e.target.value)}
            />

            <button onClick={handleAdd}>
                Add
            </button>
        </>
    )

}
export default AddIngredient