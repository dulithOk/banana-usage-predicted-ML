// export default function Input({ placeholder, className = "" }) {
//     return (
//       <input
//         type="text"
//         placeholder={placeholder}
//         className={`w-full p-2 border rounded-md bg-white/80 backdrop-blur-sm ${className}`}
//       />
//     )
//   }
  
// Input.js
export default function Input({ name, value, onChange, placeholder }) {
  return (
    <input
      type="text"
      name={name}
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      className="w-full p-2 border rounded"
    />
  );
}
  