import './App.css'
import {Providers} from "app/providers/providers.tsx";
import {AppRouter} from "app/routes";

function App() {

  return (
    <Providers>
      <AppRouter/>
    </Providers>
  )
}

export default App
