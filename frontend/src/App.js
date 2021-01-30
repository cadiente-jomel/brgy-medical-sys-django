import Navigation from './components/Navigation'

const App = () => {
  const name = 'Jomel'
  return (
    <div className="App">
      <Navigation title='Welcome' />
      <h1>Hello From react</h1>
      <h2>Hello {name}</h2>
    </div>
  );
}

export default App;

