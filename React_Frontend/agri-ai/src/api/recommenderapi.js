import axios from "axios"

export default axios.create({
    baseURL:"https://agriculture-api.herokuapp.com",
    headers: { "Content-Type": "multipart/form-data" },
})