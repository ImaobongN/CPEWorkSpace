clc; clear all;

data = readtable('data.txt'); 
data_PPM = data{:,2};
B = regexp(data_PPM,'\d\S*','Match');
PPM = cellfun(@(x)str2double(x), B);
plot (smoothdata(PPM));
xlabel('Concentration in PPM')

