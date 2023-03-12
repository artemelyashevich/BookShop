import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getAllBooks } from "../redux/products";
import "./static/item.scss";

export default function Items() {
  const { books, status, error } = useSelector((store) => store.products);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllBooks());
  }, []);
  console.log(books);

  return (
    <>
      <div className="items">
        {error ? error : ""}
        {status === "loading" && "...loading"}
        <ul>
          {books.map((item) => (
            <li className="item" key={item["id"]}>
                <img src={item["img"]} alt="" />
                <p className="title">{item["title"]}</p>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
}
