import { NavbarComponent } from "./components/NavbarComponent.js";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { LandingPage } from "./pages/LandingPage.js";
import { CaseBasedPage } from "./pages/CaseBasedPage.js";
import { RuleBasedPage } from "./pages/RuleBasedPage.js";
import { JudgmentPage } from "./pages/JudgmentPage.js";
import { LawPage } from "./pages/LawPage.js";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <div className="App">
      <NavbarComponent />
      <BrowserRouter>
        <Routes>
          <Route element={<LandingPage />} path="/home" />
          <Route element={<RuleBasedPage />} path="/rule-based" />
          <Route element={<CaseBasedPage />} path="/case-based" />
          <Route element={<JudgmentPage />} path="/judgments" />
          <Route element={<LawPage />} path="/laws" />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
