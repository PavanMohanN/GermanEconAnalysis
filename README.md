# Decomposing Economic Indicators: A Study of Compensation, GDP, and Employment Rate in Germany Through Empirical Mode Decomposition
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EMD Analysis README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2 {
            color: #333;
        }
        code {
            background: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
        .note {
            background: #f9f9f9;
            border-left: 3px solid #ccc;
            padding: 10px;
            margin: 10px 0;
        }
        .requirements, .usage, .data {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>EMD Analysis README</h1>

    <h2>Overview</h2>
    <p>This README provides instructions and explanations for the Python and MATLAB code used for analyzing economic data through Empirical Mode Decomposition (EMD). The analysis involves processing datasets related to Employment Rate, GDP, and Compensation in Germany, performing EMD, and visualizing the results.</p>

    <h2>Files</h2>
    <ul>
        <li><strong>Python Code:</strong> <code>emd_analysis.py</code></li>
        <li><strong>MATLAB Code:</strong> <code>analysis.m</code></li>
        <li><strong>Data Files:</strong>
            <ul>
                <li><code>/content/Employement Germany Modified.csv</code></li>
                <li><code>/content/GDP Germany Modified.csv</code></li>
                <li><code>/content/Compensation Germany Modified.csv</code></li>
            </ul>
        </li>
    </ul>

    <h2>Python Code: <code>emd_analysis.py</code></h2>
    <p><strong>Description:</strong></p>
    <ul>
        <li><strong>Data Collection and Preprocessing:</strong> Loads data from CSV files, drops unnecessary columns, and merges the datasets on the 'Financial Quarter'.</li>
        <li><strong>Empirical Mode Decomposition (EMD):</strong> Applies EMD to the GDP, Compensation, and Employment Rate data to decompose the time series into Intrinsic Mode Functions (IMFs).</li>
        <li><strong>Analysis and Visualization:</strong> Plots the original signals and their IMFs for each dataset. Saves the plots and analysis results as PNG and CSV files.</li>
    </ul>

    <h2>MATLAB Code: <code>analysis.m</code></h2>
    <p><strong>Description:</strong></p>
    <ul>
        <li><strong>Data Collection and Preprocessing:</strong> Loads data from CSV files, drops unnecessary columns, and merges datasets.</li>
        <li><strong>Empirical Mode Decomposition (EMD):</strong> Applies EMD to the GDP, Compensation, and Employment Rate data.</li>
        <li><strong>Analysis and Visualization:</strong> Plots the original signals and their IMFs for each dataset.</li>
    </ul>

    <h2>Requirements</h2>
    <div class="requirements">
        <h3>Python</h3>
        <ul>
            <li>Python 3.x</li>
            <li>Libraries: <code>pandas</code>, <code>matplotlib</code>, <code>PyEMD</code></li>
            <li>Install libraries using pip:</li>
            <pre><code>pip install pandas matplotlib EMD-signal</code></pre>
        </ul>

        <h3>MATLAB</h3>
        <ul>
            <li>MATLAB with EMD Toolbox or equivalent.</li>
            <li>Adjust the path to include the EMD toolbox if needed.</li>
        </ul>
    </div>

    <h2>Data</h2>
    <div class="data">
        <p>Ensure data files are available at the specified paths. The data should include columns:</p>
        <ul>
            <li><code>'Financial Quarter'</code></li>
            <li><code>'Employement Rate'</code></li>
            <li><code>'GDP'</code></li>
            <li><code>'Compensation in Billions'</code></li>
        </ul>
    </div>

    <h2>Usage</h2>
    <div class="usage">
        <h3>Python</h3>
        <ul>
            <li>Ensure all dependencies are installed.</li>
            <li>Update file paths if necessary.</li>
            <li>Run the script using Python:</li>
            <pre><code>python emd_analysis.py</code></pre>
        </ul>

        <h3>MATLAB</h3>
        <ul>
            <li>Ensure EMD toolbox is added to MATLAB path.</li>
            <li>Update file paths if necessary.</li>
            <li>Run the script in MATLAB.</li>
        </ul>
    </div>

    <h2>Notes</h2>
    <div class="note">
        <p>Verify that the data files are in the correct format and path before running the scripts. Adjust plot styles and analysis as needed based on specific requirements.</p>
    </div>

    <p>For further assistance or questions, please contact [Your Contact Information].</p>
</body>
</html>
