const varieties = [
    "Anamalu",
    "Kandula",
    "Kolikuttu",
    "Rath Kesel",
    "Sini Kesel",
    "Suwandal",
    "Ambul Nadee",
    "Ambul Kesel",
    "Puwalu",
    "Green Banana",
    "Seeni Parakum",
    "Ambum",
    "Nethra Palam",
    
  ]

  const period = [
    "January-December",
    "November-January",
  ]
  
  export default function VarietiesList() {
    return (
      <div className="mb-6">
        <h2 className="font-semibold mb-2 ml-4">Varieties:</h2>
        <ul className="space-y-2">
          {varieties.map((variety, index) => (
            <li key={index}
            className="flex items-center space-x-3 text-gray-700 text-sm font-medium"
            >
              {index + 1}. {variety}
              
            </li>
          ))}
        </ul>
        <h2 className="font-semibold mb-2 ml-4">Period:</h2>
        <ul className="space-y-2">
          {period.map((variety, index) => (
            <li key={index}
            className="flex items-center space-x-3 text-gray-700 text-sm font-medium -ml-4"
            >
              {index + 1}. {variety}
              
            </li>
          ))}
        </ul>
      </div>
    )
  }
  
  