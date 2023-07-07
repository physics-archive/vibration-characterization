function createfigureOctDat(X1, Y1, X2, Y2)
%CREATEFIGURE1(X1, Y1)
%  X1:  vector of x data
%  Y1:  vector of y data

%  Auto-generated by MATLAB on 02-May-2021 04:50:05

% Create figure
figure1 = figure;

% Create axes
axes1 = axes('Parent',figure1);
hold(axes1,'on');

% Create loglog
loglog(X1,Y1,X2,Y2,...
    'MarkerFaceColor',[0.149019607843137 0.149019607843137 0.149019607843137],...
    'MarkerEdgeColor','none',...
    'MarkerSize',4,...
    'Marker','o',...
    'Color','#32977E');

% Create yline
yline(1.95e-07,'Parent',axes1,...
    'Color',[0.635294117647059 0.0784313725490196 0.184313725490196],...
    'LabelHorizontalAlignment','left',...
    'FontSize',8,...
    'Label','VC-I');

% Create yline
yline(3.9e-07,'Parent',axes1,...
    'Color',[0.635294117647059 0.0784313725490196 0.184313725490196],...
    'LabelHorizontalAlignment','left',...
    'FontSize',8,...
    'Label','VC-H');

% Create yline
yline(7.8e-07,'Parent',axes1,...
    'Color',[0.635294117647059 0.0784313725490196 0.184313725490196],...
    'LabelHorizontalAlignment','left',...
    'FontSize',8,...
    'Label','VC-G');

% Create yline
yline(1.56e-06,'Parent',axes1,...
    'Color',[0.635294117647059 0.0784313725490196 0.184313725490196],...
    'LabelHorizontalAlignment','left',...
    'FontSize',8,...
    'Label','VC-F');

% Create yline
yline(3.12e-06,'Parent',axes1,...
    'Color',[0.635294117647059 0.0784313725490196 0.184313725490196],...
    'LabelHorizontalAlignment','left',...
    'FontSize',8,...
    'Label','VC-E');


% Create yline
yline(5e-05,'Parent',axes1,...
    'Color',[0.188235294117647 0.164705882352941 0.36078431372549],...
    'LabelHorizontalAlignment','left',...
    'FontSize',8,...
    'Label','VC-A');

% Create yline
yline(0.0001,'Parent',axes1,...
    'Color',[0.188235294117647 0.164705882352941 0.36078431372549],...
    'LabelHorizontalAlignment','left',...
    'FontSize',8,...
    'Label','Op. Theatre (ISO)');

% Create yline
yline(0.0002,'Parent',axes1,...
    'Color',[0.188235294117647 0.164705882352941 0.36078431372549],...
    'LabelHorizontalAlignment','left',...
    'FontSize',8,...
    'Label','Residential Day (ISO)');

% Create yline
yline(0.0004,'Parent',axes1,...
    'Color',[0.188235294117647 0.164705882352941 0.36078431372549],...
    'LabelHorizontalAlignment','left',...
    'FontSize',8,...
    'Label','Office (ISO)');

% Create ylabel
ylabel({'\surdPSD(v) (m/s rms)'});

% Create xlabel
xlabel({'Frequency (Hz)'});

% Create title
title({'Position 1 Data'});

box(axes1,'on');
hold(axes1,'off');
% Set the remaining axes properties
set(axes1,'XMinorTick','on','XScale','log','YMinorTick','on','YScale','log');

yline(10^-7, '-','VC-J','LabelHorizontalAlignment','left','FontSize',8,'Color',[0.635294117647059 0.0784313725490196 0.184313725490196]);


ylim([5*10^-9 3e-5]);
xlim([1 220]);
legend('X Ground (Paper)','Position 1 Data');
%createfigureOctDat(cfreQ(2:17),ans(2:17),cfreq('m10s',10,10,5000,500),octSort('m10s',10,10,5000,500))