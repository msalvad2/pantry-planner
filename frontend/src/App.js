import { BrowserRouter, Route, Routes, Link } from "react-router-dom"
import { useEffect, useState } from "react"

import Pantry from "./pages/Pantry"
import Home from "./pages/Home"
import ShoppingList from "./pages/ShoppingList"
import Recipes from "./pages/Recipes"
import client from "./api/client"

function App() {

  const [ingredients, setIngredients] = useState([])

  async function fetchPantry(){
    const res = await client.get("/pantry")
    setIngredients(res.data)
  }

  //get method to retrieve the entire pantry items and store them in ingredients
  useEffect(() => {
    async function loadPantry(){
      try{
      const res = await client.get("/pantry")
      setIngredients(res.data)
      } catch(err) {
        console.error("Failed to load pantry: ", err)
      }
    }
    //call function
    loadPantry()
  }, [])

  //function used to add new ingredients
  async function addItem(newItem) {
    const cleaned = newItem.trim().toLowerCase()
    if (cleaned === "") return

    //add the item to the backend
    try{
    await client.post("/pantry", {name: cleaned})

    //re-fetch backend truth: replace frontend state with updated backend data
    fetchPantry()

    } catch(err){
      console.error("Failed to add item", err)
    }
  }

  //removes item on backend server
  async function removeItem(idToRemove) {
    try{
    //send delete request
    await client.delete(`/pantry/${idToRemove}`)

    //re-fetch backend data to update fronted state
    fetchPantry()

  }catch(err){
    console.error("Failed to remove item", err)
  }
  }

  //Update item on backened server
  async function editItem(newName, id) {
    const cleaned = newName.trim()

    if (cleaned === "") return
    try{
    //update item on backend server
    await client.put(`pantry/${id}`, {name: cleaned})
    //refetch data to update frontend state
      fetchPantry()

    } catch(err){
      console.error("Failed to update item", err)
    }
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























