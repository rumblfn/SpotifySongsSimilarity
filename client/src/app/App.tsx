import './App.css'
import {Providers} from "app/providers/providers.tsx";
import {AppRouter} from "app/routes";
import {Header} from "shared/ui/header";

function App() {
  return (
    <Providers>
      <div className="app-wrapper">
        <Header />
        <AppRouter />
      </div>
    </Providers>
  )
}

export default App
