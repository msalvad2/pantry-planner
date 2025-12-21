
import Pantry from "./pages/Pantry"
import Home from "./pages/Home"
import ShoppingList from "./pages/ShoppingList"
import Recipes from "./pages/Recipes"
import { BrowserRouter, Route, Routes, Link } from "react-router-dom"
import { useEffect, useState } from "react"


function App() {

  const [ingredients, setIngredients] = useState([])

  //get method to retrieve the entire pantry items and store them in ingredients
  useEffect(() => {
    fetch("http://localhost:8000/pantry")
      .then(res => res.json())
      .then(data => setIngredients(data))
  }, [])

  //function used to add new ingredients
  async function addItem(newItem) {
    const cleaned = newItem.trim()
    if (cleaned === "") return

    //add the item to the backend
    await fetch("http://localhost:8000/pantry", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({name: cleaned})
    })

    //re-fetch backend truth: replace frontend state with updated backend data
    const res = await fetch("http://localhost:8000/pantry")
    const data = await res.json()
    setIngredients(data)
  }

  function removeItem(indexToRemove) {
    setIngredients(ingredients.filter((element) => element.id !== indexToRemove))
  }

  function editItem(newName, id) {
    const cleaned = newName.trim()

    if (cleaned == "") return

    setIngredients(ingredients.map(item => {
      if (item.id === id) {

        return {
          ...item,
          name: cleaned
        }
      }
      return (
        item
      )
    }))
  }

  return (
    <BrowserRouter>

      <nav>
        <ul>
          <li>  <Link to="/"> Home</Link> </li>
          <li> <Link to="/recipes"> Recipes</Link> </li>
          <li>  <Link to="/shopping-list">Shopping List</Link> </li>
          <li>  <Link to="/pantry"> Pantry </Link> </li>
        </ul>

      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/recipes" element={<Recipes />} />
        <Route path="/shopping-list" element={<ShoppingList />} />
        <Route path="/pantry" element={
          <Pantry
            ingredients={ingredients}
            onAdd={addItem}
            onRemove={removeItem}
            onEdit={editItem}
          />} />
      </Routes>

    </BrowserRouter>

  )
}



export default App























