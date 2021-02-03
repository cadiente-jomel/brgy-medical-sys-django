import Navigation from './components/Navigation';
import Search from './components/Search';
import BreadCrumbs from './components/BreadCrumbs';
import Dropdown from './components/Dropdown';
import Main from './components/Main';
import Title from './components/Title';
import Stats from './components/Stats';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";


const App = () => {
  return (
    <Router>
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
                  <div className='content overflow-auto'>
                      <Switch >
                          <Route exact path='/'>
                              <Title/> 
                              <Stats />
                              <h4 className='pl-4'>Recently Added Record</h4>
                              <Main view='dashboard'/>
                          </Route>
  
                          <Route exact path='/citizen-profile'>
                              <Title title='Citizen Profile' icon='fas fa-users citizen mr-2 text-default'  btnText='Add Record' btnIcon='fas fa-plus mr-2'/> 
                              <Main view='citizen-rec'/>
                          </Route>
                          <Route exact path='/citizen-check-up'>
                              <Title title='Check Up Records' icon='fas fa-notes-medical checkup mr-2 text-default'  btnText='Add Record' btnIcon='fas fa-plus mr-2'/> 
                              <Main view='check-up'/>
                          </Route>
                          <Route exact path='/pandemic-records'>
                              <Title title='Pandemic Records' icon='fas fa-head-side-cough pandemic mr-2 text-default'  btnText='Add Record' btnIcon='fas fa-plus mr-2'/> 
                              <Main view='pandemic' />
                          </Route>
                      </Switch>
                  </div>
              </div>
          </div>
        </div>
    </Router>
  );
}

export default App;

