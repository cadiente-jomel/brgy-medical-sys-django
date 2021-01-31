//  props types
import PropTypes from 'prop-types';
import React from 'react';
import Button from './Button'

// navigation should be vertical
const Navigation = ({ title }) => {
    return (
        <nav style={navigationStyle} className='flex flex-col justify-between w-20 h-screen navigation navigation--theme-default '>
        {/* inline styling */}
            <div className="flex flex-col navigation__container">
                <a href="/" style={homeButtonStyle} className='navigation__home'>Home</a>
                <Button icon='fas fa-home home'  text='Home'/>
                <Button icon='fas fa-users navigation__citizen'  text='Citizen Profile'/>
                <Button icon='fas fa-notes-medical navigation__checkup'  text='Check Up'/>
                <Button icon='fas fa-money-bill-alt navigation__expenses'  text='Medical Expenses'/>
                <Button icon='fas fa-head-side-cough navigation__pandemic'  text='Pandemic Records'/>
            </div>
                <div className="navigation__bottom__el navigation__settings ">
                    <Button icon='fas fa-cog'  text='Pandemic Records' btncls='btn btn--bottom p-4'/>
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
    backgroundColor: '#f2f2f1',
}

const homeButtonStyle = {
    color: '#fff',
    backgroundColor: '#dd3422',
    textAlign: 'center',
    textTransform: 'uppercase',
    padding: '.8rem',
    height: '3rem',
}
export default Navigation
