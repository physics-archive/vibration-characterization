function Plotnb(X1, Y1)
%CREATEFIGURE(X1, Y1)
%  X1:  vector of x data
%  Y1:  vector of y data

%  Auto-generated by MATLAB on 28-Jun-2021 17:33:42

% Create figure
figure1 = figure;

% Create axes
axes1 = axes('Parent',figure1);
hold(axes1,'on');

% Create loglog
loglog(X1,Y1,'Color',[0.4940, 0.1840, 0.5560]);

% Uncomment the following line to preserve the X-limits of the axes
% xlim(axes1,[1 125]);
% Uncomment the following line to preserve the Y-limits of the axes
% ylim(axes1,[1e-10 0.0001]);
box(axes1,'on');
hold(axes1,'off');
% Set the remaining axes properties
set(axes1,'XMinorTick','on','XScale','log','YMinorTick','on','YScale','log');
yline(1e-6);
yline(1e-7);
yline(1e-8);
yline(1e-9);
xline(1);
xline(10);
xline(100);
xlim([1 130]);
ylim([1e-10 1e-4]);
% ylabel
ylabel({'\surdPSD(v) (m/s/\surdHz)'});
% Create xlabel
xlabel({'Frequency (Hz)'});