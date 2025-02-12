import { useState } from "react";
import Button from "./Button";
import Input from "./Input";
import VarietiesList from "./VarietiesList";

export default function Home() {
  // State to hold form data
  const [formData, setFormData] = useState({
    variety_name: "",
    quantity: "",
    period: "",
  });

  // State for error handling and success messages
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const [apiResponse, setApiResponse] = useState(null);

  // Update form data when inputs change
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  // Submit form data to backend
  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrorMessage("");
    setSuccessMessage("");

    // Validate inputs
    if (!formData.variety_name || !formData.quantity || !formData.period) {
      setErrorMessage("All fields are required.");
      return;
    }

    if (isNaN(formData.quantity)) {
      setErrorMessage("Quantity must be a number.");
      return;
    }

    try {
      console.log("########## get the data ", formData);
      const response = await fetch("http://localhost:8006/v1/banana/get", {
        method: "POST", // Use POST to send data
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          variety_name: formData.variety_name,
          quantity: parseInt(formData.quantity, 10), // Convert quantity to integer
          period: formData.period,
        }),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      const data = await response.json();
      setSuccessMessage("Data sent successfully!");
      setApiResponse(data); // Save API response to state
      console.log("Response from server:", data);
    } catch (error) {
      setErrorMessage(`Failed to send data: ${error.message}`);
    }
  };

  return (
    <div
      className="min-h-screen bg-cover bg-center p-4"
      style={{
        backgroundImage:
          'url("https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTA4L3Jhd3BpeGVsX29mZmljZV8yNF8zZF9yZW5kZXJfaWxsdXN0cmF0aW9uX29mX2FuX2VtcHR5X2JhbmFuYV9wbF80YmY5ZGNiNi02MzMwLTQ0NGItYjY5OS1jNDBjYTk1Y2FmOTNfMS5qcGc.jpg")',
      }}
    >
      <div className="max-w-md mx-auto bg-white/90 backdrop-blur-sm p-6 rounded-lg shadow-lg flex items-center justify-center min-h-[300px]">
        {apiResponse ? (
          <div className="p-6 bg-white/90 backdrop-blur-sm rounded-lg shadow-md text-center">
            <h2 className="text-lg font-semibold text-green-700 mb-4">Response</h2>
            <p className="text-sm text-gray-700 mb-2">
              <strong>Success:</strong> {successMessage}
            </p>
            <p className="text-sm text-gray-700 mb-2">
              <strong>Predicted Use:</strong> {apiResponse.results.predicted_use}
            </p>
            <p className="text-sm text-gray-700">
              <strong>Confidence Score:</strong> {apiResponse.results.confidence_score.toFixed(2)}
            </p>
            <button
            onClick={() => {
              setApiResponse(null); // Clear the response state
              setFormData({ variety_name: "", quantity: "", period: "" }); // Reset the form data
            }}
            className="mt-4 px-4 py-2 bg-green-600 text-white rounded-lg shadow-md hover:bg-green-700 transition duration-300"
          >
            Add Data
          </button>
          </div>
          
        ) : (
          
          <div className="flex flex-col items-center justify-center">
            
            <VarietiesList />

            <form onSubmit={handleSubmit} className="space-y-4">
              <Input
                name="variety_name"
                placeholder="Poovan"
                value={formData.variety_name}
                onChange={handleInputChange}
              />
              <Input
                name="quantity"
                placeholder="1000"
                value={formData.quantity}
                onChange={handleInputChange}
              />
              <Input
                name="period"
                placeholder="January-December"
                value={formData.period}
                onChange={handleInputChange}
              />
              <Button type="submit" className="mb-6">
                Generate Sales
              </Button>
            </form>

            {errorMessage && (
              <div
                className="p-4 mb-4 text-sm text-red-700 bg-red-100 rounded-lg"
                role="alert"
              >
                <span className="font-medium">Error:</span> {errorMessage}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
