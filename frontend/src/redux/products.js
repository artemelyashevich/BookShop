import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import axios from "axios";

export const getAllBooks = createAsyncThunk(
  "products/getAllBooks",
  async (_, { rejectWithValue }) => {
    try {
      const res = await axios("http://127.0.0.1:5000/books");
      if (res.status !== 200) {
        throw new Error("Server error!");
      }
      return res.data;
    } catch (error) {
      console.log(error);
      return rejectWithValue(error.message);
    }
  }
);

const products = createSlice({
  name: "products",
  initialState: {
    books: [],
    filter: {
      price: {
        from: 0,
        to: 100,
      },
    },
    productsLength: 0,
    status: "",
    error: "",
  },
  reducers: {},
  extraReducers: {
    [getAllBooks.pending]: (state, action) => {
      state.status = "loading";
    },
    [getAllBooks.rejected]: (state, action) => {
      state.status = "rejected";
      state.error = action.payload;
    },
    [getAllBooks.fulfilled]: (state, action) => {
      state.status = "success";
      state.books = action.payload;
    },
  },
});

export default products.reducer;
export const { countTestClicked, addNewPetr, deletePetr, addName } =
  products.actions;
