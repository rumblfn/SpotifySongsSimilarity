import {createBrowserRouter, RouterProvider} from "react-router-dom";
import {MapOfSpotifyPage} from "pages/map-of-spotify";

const router = createBrowserRouter([
  {
    path: "/",
    element: <MapOfSpotifyPage />,
  },
]);

export const AppRouter = () => {
  return (
    <div className="page">
      <RouterProvider router={router} />
    </div>
  )
}