import PropTypes from 'prop-types';

const Button = ({ icon, text, color}) => {
    return <button style={{backgroundColor: color}}><i className={icon}></i> {text}</button>
}

Button.propTypes = {
    color: PropTypes.string,
    icon: PropTypes.string.isRequired,
}

export default Button