adaptation = zeros(4,72,24);
for participant = 1:24
    
    fprintf('Loading the data of participant %d in the memory updating experiment\n',participant)
    
    % load participant's data
    load(sprintf('memory_updating_participant%d.mat',participant),'TrialData')
    
    % find channel trials
    channel_trials = find(~isnan(TrialData.Adaptation));
    
    % determine the control point that is presented on the channel trials
    % of triplets (so-called cue 1) 
    triplet_trial = find(strcmp(TrialData.BlockName,'Triplet1'),1,'first');
    cue_1 = TrialData.ControlPoint(triplet_trial);
    
    % determine the direction of the field that is paired with cue 1 on
    % exposure trials (so-called P^+)
    exposure_trial_cue_1 = find(TrialData.ControlPoint==cue_1 & strcmp(TrialData.BlockName,'Exposure'),1,'first');
    P_plus = sign(TrialData.FieldConstants(exposure_trial_cue_1,1));
    
    cnt = zeros(1,6);
    for i = 1:numel(channel_trials)
        
        % current channel trial
        trial = channel_trials(i);
        
        if contains(TrialData.BlockName{trial},'Triplet') % channel-exposure-channel triplet of trials
            
            if ~mod(sum(cnt(1:4)),2)
                exposure_trial = trial + 1; % trial is the first channel trial of the triplet (i.e. the trial before the exposure trial)
            else                
                exposure_trial = trial - 1; % trial is the second channel trial of the triplet (i.e. the trial after the exposure trial)
            end
            
            % field direction on exposure trial
            perturbation_sign = sign(TrialData.FieldConstants(exposure_trial,1));
            
            % cue on exposure trial
            cue = TrialData.ControlPoint(exposure_trial);
            
            if perturbation_sign==P_plus && cue==cue_1     % exposure trial is P^+_1
                p = 1;
            elseif perturbation_sign==P_plus && cue~=cue_1 % exposure trial is P^+_2
                p = 2;
            elseif perturbation_sign~=P_plus && cue==cue_1 % exposure trial is P^-_1
                p = 3;
            elseif perturbation_sign~=P_plus && cue~=cue_1 % exposure trial is P^-_2
                p = 4;
            end
            
        elseif strcmp(TrialData.BlockName{trial},'Double') % channel-channel double of trials (before and after each block of exposure trials)
            
            % cue on channel trial
            cue = TrialData.ControlPoint(trial);
            
            if cue==cue_1
                p = 5; % cue 1 channel trial
            else
                p = 6; % cue 2 channel trial
            end
            
        end
        cnt(p) = cnt(p) + 1;
        
        % extract adaptation data (adjust sign based on counterbalanced P^+ field direction)
        adaptation(p,cnt(p),participant) = P_plus*TrialData.Adaptation(channel_trials(i));
        
    end
    
end

% single-trial learning
single_trial_learning{1} =  squeeze(sum([-1 1]'.*reshape(adaptation(1,:,:),2,36,24)));    % single-trial learning for the P^+_1 triplet
single_trial_learning{2} =  squeeze(sum([-1 1]'.*reshape(adaptation(2,1:24,:),2,12,24))); % single-trial learning for the P^+_2 triplet
single_trial_learning{3} = -squeeze(sum([-1 1]'.*reshape(adaptation(3,1:24,:),2,12,24))); % single-trial learning for the P^-_1 triplet (sign inverted)
single_trial_learning{4} = -squeeze(sum([-1 1]'.*reshape(adaptation(4,:,:),2,36,24)));    % single-trial learning for the P^-_2 triplet (sign inverted)

figure
set(0,'DefaultFigureColor',[1 1 1])
fig = gcf;
fig.Position(3:4) = [300 420];

subplot(2,1,1)
std_data = normalised_standard_deviation_of_data(single_trial_learning,'pre-training');
plot_data(single_trial_learning,std_data,'pre-training')

subplot(2,1,2)
std_data = normalised_standard_deviation_of_data(single_trial_learning,'post-training');
plot_data(single_trial_learning,std_data,'post-training')

function std_data = normalised_standard_deviation_of_data(data,phase)

    % relevant blocks of trials
    if strcmp(phase,'pre-training')
        blocks{1} = 1:4;
        blocks{2} = 1:4;
        blocks{3} = 1:4;
        blocks{4} = 1:4;
    elseif strcmp(phase,'post-training')
        blocks{1} = 29:36;
        blocks{2} = 5:12;
        blocks{3} = 5:12;
        blocks{4} = 29:36;
    end

    % standard deviation of the data
    std_data = zeros(1,4);
    for i = 1:4
        std_data(i) = std(mean(data{i}(blocks{i},:)));
    end
    
    % normalised standard deviation of the data
    std_data = std_data/max(std_data);

end

function plot_data(data,std_data,phase)

    % plot variables
    line_width = 1.5;
    marker_size = 15;
    font_size = 15;
    bar_width = 0.8;
    colours = [0.1216    0.4706    0.7059
               0.5059    0.2863    0.4078
               0.5059    0.2863    0.4078
               0.8902    0.1020    0.1098];
           
    % relevant blocks of trials
    if strcmp(phase,'pre-training')
        blocks{1} = 1:4;
        blocks{2} = 1:4;
        blocks{3} = 1:4;
        blocks{4} = 1:4;
    elseif strcmp(phase,'post-training')
        blocks{1} = 29:36;
        blocks{2} = 5:12;
        blocks{3} = 5:12;
        blocks{4} = 29:36;
    end
    
    hold on
    plot([0 5],[0 0],'k')
    for i = 1:4
        
        % summary statistics
        individual_mean = mean(data{i}(blocks{i},:));
        overall_mean = mean(data{i}(blocks{i},:),'all');
        SEM = std(mean(data{i}(blocks{i},:)))/sqrt(24);

        % SEM error bars
        errorbar(i,overall_mean,zeros(size(SEM)),SEM,'color',colours(i,:),'LineWidth',line_width)
        
        % mean bars
        patch([i-bar_width/2 i+bar_width/2 i+bar_width/2 i-bar_width/2],[overall_mean overall_mean 0 0],colours(i,:),'EdgeColor',colours(i,:),'LineWidth',line_width);
        
        % scatter plot for individual participant data
        % horizontal spread reflects the standard deviation of the data
        width = std_data(i)*0.5;
        scatter(i+rand(1,24)*width-width/2,individual_mean,marker_size,'o','MarkerEdgeColor','k','MarkerEdgeAlpha',0.2,'LineWidth',0.25,'MarkerFaceColor',colours(i,:),'MarkerFaceAlpha',0.2)
        
        box('off')
        axis([0 5 -0.25 .46])
        if strcmp(phase,'pre-training')
            ylabel({'{\bfpre-training}'});
            set(gca,'FontSize',font_size,'LineWidth',line_width,'YTick',[0 .4],'XTick',[])
            title('single-trial learning (for context 1)');
        elseif strcmp(phase,'post-training')
            ylabel({'{\bfpost-training}'});
            set(gca,'FontSize',font_size,'LineWidth',line_width,'YTick',[0 .4],'XTick',[1 2 3 4],'XTickLabels',{'P^+_1' 'P^+_2' 'P^-_1' 'P^-_2'},'TickLength',[0 0])
        end
        
    end

end