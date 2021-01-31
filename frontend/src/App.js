import Navigation from './components/Navigation'
import Search from './components/Search'
import BreadCrumbs from './components/BreadCrumbs'
import Dropdown from './components/Dropdown'
import Title from './components/Title'
import Stats from './components/Stats'
import Table from './components/Table'

const App = () => {
  return (
    <div className="App flex">
    <div className="left">
      <Navigation />
    </div>
      <div className='w-screen right'>
          <Search />
          <div className="right__main">
              <div className='container mx-auto flex justify-between items-center' >
                  <BreadCrumbs />
                  <Dropdown />
              </div>
              <div className="content overflow-auto">  
                <Title />
                <Stats />
                <h4 className='pl-5'>Recently Added Record</h4>
                <Table />
              </div>
          </div>
      </div>
    </div>
  );
}

export default App;

