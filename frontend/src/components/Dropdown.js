const onClick = () => {
    let btnDropdown
    if (document.querySelector('.origin-top-right')) {
        btnDropdown = document.querySelector('.ddbtn');
        // alert('True')
        // btnDropdown = 
        btnDropdown.classList.remove('origin-top-right')
        btnDropdown.classList.add('origin-top-right--show')
        // flag = false
    } else {
        btnDropdown = document.querySelector('.ddbtn');
        // alert('False')
        // btnDropdown = document.querySelector('.origin-top-right--show')
        btnDropdown.classList.remove('origin-top-right--show')
        btnDropdown.classList.add('origin-top-right')
    
        // flag = true
    }
    // alert('outside')
}

const Dropdown = () => {
    return (
    
        <div className="relative inline-block text-left">
        <div>
            <button type="button" onClick={onClick} className="inline-flex justify-center w-full rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-indigo-500" id="options-menu" aria-haspopup="true" aria-expanded="true">
            Options
            {/* <!-- Heroicon name: chevron-down --> */}
            <svg className="-mr-1 ml-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
            </svg>
            </button>
        </div>

        {/* <!--
            Dropdown panel, show/hide based on dropdown state.

            Entering: "transition ease-out duration-100"
            From: "transform opacity-0 scale-95"
            To: "transform opacity-100 scale-100"
            Leaving: "transition ease-in duration-75"
            From: "transform opacity-100 scale-100"
            To: "transform opacity-0 scale-95"
        --> */}
        <div className="origin-top-right ddbtn absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5">
            <div className="py-1" role="menu" aria-orientation="vertical" aria-labelledby="options-menu">
            <a href="/" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900" role="menuitem">Account settings</a>
            <a href="/" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900" role="menuitem">Support</a>
            <a href="/" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900" role="menuitem">License</a>
            <form method="POST" action="#">
                <button type="submit" className="block w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900 focus:outline-none focus:bg-gray-100 focus:text-gray-900" role="menuitem">
                Sign out
                </button>
            </form>
            </div>
        </div>
        </div>
    )
}

export default Dropdown;