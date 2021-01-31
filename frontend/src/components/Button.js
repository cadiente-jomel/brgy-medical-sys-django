import PropTypes from 'prop-types';

const Button = ({ btncls, icon, text, color}) => {
    return <button className={btncls  ? btncls : 'btn p-4 text-red-600' } style={{backgroundColor: color}}><i className={icon}></i></button>
}

Button.propTypes = {
    color: PropTypes.string,
    icon: PropTypes.string.isRequired,
}

Button.defaultProps = {
    color: 'transparent',
}

export default Button