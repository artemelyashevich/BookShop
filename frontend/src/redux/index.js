import {configureStore} from "@reduxjs/toolkit";
import products from './products'

const store = configureStore({
    reducer: {
        products: products
    }
})

export default store