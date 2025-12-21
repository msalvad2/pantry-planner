
import AddIngredient from "../AddIngredient"
import IngredientList from "../IngredientList"

function Pantry({ ingredients, onAdd, onRemove, onEdit}) {



    
    return (
        <>
            <h2>My Pantry</h2>

            <IngredientList items={ingredients} onRemove={onRemove} onEdit={onEdit}/>
            <AddIngredient onAdd={onAdd} />

        </>

    )
}
export default Pantry