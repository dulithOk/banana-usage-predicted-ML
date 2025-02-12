export default function Button({ children, onClick, className = "" }) {
    return (
      <button
        onClick={onClick}
        className={`w-full bg-green-500 text-white py-2 px-4 rounded-md hover:bg-green-600 transition-colors ${className}`}
      >
        {children}
      </button>
    )
  }
  
  