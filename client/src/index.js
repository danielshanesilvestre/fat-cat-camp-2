import React from "react";
import "./index.css";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from 'react-router';

import App from "./components/App";
import OwnersIndex from "./components/pages/OwnersIndex"

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    children: [
      {
        path: "/",
        element: <h1>Home</h1>
      },
      {
        path: "/owners",
        element: <OwnersIndex />
      }
    ]
  }
]);

const root = createRoot(document.getElementById("root"));

root.render(
    <React.StrictMode>
      <RouterProvider router={router} />
    </React.StrictMode>
);
