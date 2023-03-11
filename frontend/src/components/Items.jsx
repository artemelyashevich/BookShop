import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getAllBooks } from "../redux/products";
import "./static/item.css"

export default function Items() {
  const { books, status, error } = useSelector((store) => store.products);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllBooks());
  }, []);
  console.log(books);

  return (
    <>
    <div className="item">
    {error ? error : ''}
      {status === 'loading' && '...loading'}
      <ul>
        {books.map((item) => (
          <li key={item["id"]}><p>{item["title"]}</p>
          <img src={item["img"]} alt="" />
          </li>
        ))}
      </ul>

    </div>
  
    </>
  );
}
