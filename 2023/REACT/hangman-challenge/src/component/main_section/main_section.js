import React, { useState, useEffect } from "react";
import "./main_section.css"

const LANGUAGES = [
    "burger",
    // "cheese",
    // "pizza",
    // "noodle",
    // "pie",
    // "banana"
  ];

let layouts = [
  [""],
  ["", "😥", "", "", "", "", "", "", ""],
  ["", "😥", "", "-", "", "", "", "", ""],
  ["", "😥", "", "-", "|", "", "", "", ""],
  ["", "😥", "", "-", "|", "-", "", "", ""],
  ["", "😥", "", "-", "|", "-", "/", "", ""]
];

function App() {
cosnt


  const [language, setLanguage] = useState("...");
  const [letter, setLetter] = useState("GUESS!");
  const [blanks, setBlanks] = useState("");
  const [markdown, setMarkdown] = useState("");
  const [layout, setLayout] = useState(layouts[0]);
  const [gameOver, setGameOver] = useState(false);
  const [winner, setWinner] = useState(false);

  const generatePhrase = () => {
    const randomLanguage =
      LANGUAGES[Math.floor(Math.random() * LANGUAGES.length)];
    const currentBlanks = randomLanguage
      .split("")
      .map((event) => (event !== " " ? "_" : " "))
      .join("");
    setLanguage(randomLanguage);
    setBlanks(currentBlanks);
  };

  const handleKeyPress = (event) => {
    const newMarkdown = event.target.value;
    const newLetter = newMarkdown.charAt(event.target.value.length - 1);
    setMarkdown(newMarkdown);
    setLetter(newLetter);
  };


  useEffect(() => {
    if (blanks === language) {
      setWinner(true);
      layout[1] = "🤩"
      alert("YAY YOU WON!!")
    }
    if (language.includes(letter)) {
      let newBlanks = blanks
        .split("")
        .map((a, index) => (language[index] === letter ? letter : a))
        .join("");
      setBlanks(newBlanks);
    } else if (
      letter !== "TYPE AT YOUR OWN RISK!" &&
      !language.includes(letter)
    ) {
      if (layouts.length - 1 > 1) {
        layouts.shift();
        setLayout(layouts[0]);
      } else {
        setGameOver(true);
        setLayout(["", "💀", "", "🦴", "🦴", "🦴", "🦴", "", " 🦴🦴"]);
        alert("YOU LOSE!")
      }
    }
  }, [letter, blanks, language, winner]);
  useEffect(() => {
    generatePhrase();
  }, []);

  return (
    <div className="Hangman">
      <h2>
        | <br /> | <br /> | <br />
        {layout.slice(0, 3)} <br /> {layout.slice(3, 6)} <br /> {layout.slice(6, 9)}
      </h2>
      <h3 >{blanks}</h3>
      <h3>{letter}</h3>
      <input
        type="text"
        placeholder="BE CAUTIOUS!" 
        onChange={handleKeyPress}
        value={markdown}
        disabled={gameOver || winner}>
    </input>

      <div className="title">
        <h1>SAVE THE MAN FROM ETERNAL DOOM!!!</h1>
      </div>
    </div>
  );
}
export default App;