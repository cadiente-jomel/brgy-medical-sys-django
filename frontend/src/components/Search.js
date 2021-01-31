import PropTypes from 'prop-types';
import Button from './Button';

const Search = () => {
    return (
        <div style={formStyle} className='search'>
            <form  action="" className='items-center flex justify-center'>
                <input style={searchStyle} className='search__input' type="text" name="" id="" placeholder="Search Record"/>
                <Button icon='fas fa-search'  text='Pandemic Records' btncls=' btn search__btn'/>
                <Button icon='fas fa-sign-out-alt'  text='Pandemic Records' btncls=' btn search__btn'/>
            </form>
        </div>
    )
}

const searchStyle = {
    width: '90%',
    padding: '.5rem 1rem',
    height: '3rem',
}

const formStyle = {
    backgroundColor: '#fff',
    height: '3rem',
}


export default Search