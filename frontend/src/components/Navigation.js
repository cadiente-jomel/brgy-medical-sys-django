//  props types
import PropTypes from 'prop-types';
import React from 'react';
import Button from './Button'

// navigation should be vertical
const Navigation = ({ title }) => {
    return (
        <nav className='navigation navigation--theme-default'>
        {/* inline styling */}
            <div className="navigation__container">
                <a href="/" className='navigation__home'>Home</a>
                <Button icon='fas fa-home home' color='#f9c4b0' text='Home'/>
                <Button icon='fas fa-users navigation__citizen' color='#f9c4b0' text='Citizen Profile'/>
                <Button icon='fas fa-notes-medical navigation__checkup' color='#f9c4b0' text='Check Up'/>
                <Button icon='fas fa-money-bill-alt navigation__expenses' color='#f9c4b0' text='Medical Expenses'/>
                <Button icon='fas fa-head-side-cough navigation__pandemic' color='#f9c4b0' text='Pandemic Records'/>
            </div>
        </nav>
    )
}

// default props
Navigation.defaultProps = {
    title: 'Barangay'
}

// set the title props to type of strings to make it required use .isRequired
Navigation.propTypes = { 
    title: PropTypes.string.isRequired,
}

// css in js
const navigationStyle = {
    color: 'blue',
    backgroundColor: 'pink'
}
export default Navigation
