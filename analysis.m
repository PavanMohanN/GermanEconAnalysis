% Load the datasets
df1 = readtable('/content/Employement Germany Modified.csv');
df2 = readtable('/content/GDP Germany Modified.csv');
df3 = readtable('/content/Compensation Germany Modified.csv');

% Drop unnecessary columns
df1.DATE = [];
df2.DATE = [];
df3.DATE = [];
df3.Compensation = [];

% Merge datasets on 'Financial Quarter'
merged_df = join(df1, df2, 'Keys', 'FinancialQuarter');
merged_df = join(merged_df, df3, 'Keys', 'FinancialQuarter');

% Display the merged data
disp(head(merged_df))

% Add EMD toolbox to MATLAB path if needed
addpath('/path/to/EMD_toolbox');

% EMD Analysis for GDP
gdp = merged_df.GDP;
imf_gdp = emd(gdp);

% Plot the original signal and IMFs
figure;
subplot(length(imf_gdp) + 1, 1, 1);
plot(merged_df.FinancialQuarter, gdp, 'r');
title('Original Signal - GDP');

for i = 1:length(imf_gdp)
    subplot(length(imf_gdp) + 1, 1, i + 1);
    plot(merged_df.FinancialQuarter, imf_gdp{i}, 'g');
    title(['IMF ' num2str(i)]);
end

% EMD Analysis for Compensation
CIB = merged_df.CompensationInBillions;
imf_cib = emd(CIB);

% Plot the original signal and IMFs
figure;
subplot(length(imf_cib) + 1, 1, 1);
plot(merged_df.FinancialQuarter, CIB, 'r');
title('Original Signal - Compensation in Billions');

for i = 1:length(imf_cib)
    subplot(length(imf_cib) + 1, 1, i + 1);
    plot(merged_df.FinancialQuarter, imf_cib{i}, 'g');
    title(['IMF ' num2str(i)]);
end

% EMD Analysis for Employment Rate
ER = merged_df.EmployementRate;
imf_er = emd(ER);

% Plot the original signal and IMFs
figure;
subplot(length(imf_er) + 1, 1, 1);
plot(merged_df.FinancialQuarter, ER, 'r');
title('Original Signal - Employment Rate');

for i = 1:length(imf_er)
    subplot(length(imf_er) + 1, 1, i + 1);
    plot(merged_df.FinancialQuarter, imf_er{i}, 'g');
    title(['IMF ' num2str(i)]);
end

% Perform statistical analysis on IMFs (example: mean, standard deviation)
disp('Statistics for IMFs (GDP):');
for i = 1:length(imf_gdp)
    fprintf('IMF %d: Mean = %.2f, Std Dev = %.2f\n', i, mean(imf_gdp{i}), std(imf_gdp{i}));
end

% Similarly for Compensation and Employment Rate

% Example of generating a report of findings
report_data = table;
report_data.IMF = cell(length(imf_gdp), 1);
report_data.Mean = zeros(length(imf_gdp), 1);
report_data.StdDev = zeros(length(imf_gdp), 1);

for i = 1:length(imf_gdp)
    report_data.IMF{i} = ['IMF ' num2str(i)];
    report_data.Mean(i) = mean(imf_gdp{i});
    report_data.StdDev(i) = std(imf_gdp{i});
end

% Save report to CSV
writetable(report_data, '/content/IMF_Analysis_Report.csv');

disp('IMF Analysis Report Generated');
