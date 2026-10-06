####################Data visualization script for Experiment 3#######################
#Authors: Yi Zhang, Leor Hackel
#April 2025

#clear environment
rm(list = ls())

#set path to the project folder
path <- getwd()

#load required packages
library(tidyverse) #for cleaning data
library(Rmisc) #for calculating confidence interval

####################Visualization###################
#Figure 9A: Probability of optimal choice as a function of contingency reversal
data_3 <- read.csv(paste0(path, "/Experiment_3/data_clean/data_3.csv"), header = TRUE)

#remove RTs <= 200ms
data_3 <- data_3%>%
  filter(DM_choice_component.rt > 0.2)

#prepare dataset for visualization
data_3_plot <- 
  data_3%>%
  select(ID_anonymous, condition_change_recode, optimal, DM_choice_component.rt,
         contingency_awareness_1_recode)%>%
  mutate(contingency_reversal = recode(condition_change_recode, 
                                       "-1" = "No Change", "1" = "Reversal"),
         contingency_awareness = recode(contingency_awareness_1_recode,
                                        "-1" = "No", 
                                        "1" = "Yes"),
         DM_choice_component.rt.log = log(DM_choice_component.rt))%>%
  select(ID_anonymous, contingency_reversal, optimal, DM_choice_component.rt.log,
         contingency_awareness)

# Step 1: Compute per-subject mean optimal choice
df_subject <- data_3_plot %>%
  group_by(ID_anonymous, contingency_reversal) %>%
  dplyr::summarise(optimal_rate = mean(optimal), .groups = 'drop')

# Step 2: Compute group summary with 95% CI
data_3_plot_summary <- df_subject %>%
  group_by(contingency_reversal) %>%
  dplyr::summarise(
    mean_optimal = mean(optimal_rate),
    se = sd(optimal_rate) / sqrt(n()),
    ci = se * qt(0.975, df = n() - 1),
    .groups = 'drop'
  )

# Step 3: Plot
custom_colors <- c("Reversal" = "#ffbff8", "No Change" = "#87b6e8")
ggplot(data_3_plot_summary, aes(x = contingency_reversal, y = mean_optimal,
                                fill = contingency_reversal)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = custom_colors)+
  geom_errorbar(aes(ymin = mean_optimal - ci, ymax = mean_optimal + ci), width = 0.2) +
  ylab("Probability") +
  xlab("Condition")+ 
  theme(legend.position = "none")+
  ylim(c(0, 0.8))


#Figure 9B: Moderation effect of contingency awareness
data_3_plot_mod <- data_3_plot%>%
  group_by(ID_anonymous, contingency_reversal, contingency_awareness)%>%
  dplyr::summarise(prob_optimal = mean(as.numeric(as.character((optimal)), 
                                                  na.rm = TRUE)))%>%
  ungroup()

data_3_plot_summary2 <- Rmisc::summarySE(data_3_plot_mod,
                                        measurevar = "prob_optimal",
                                        groupvars =  c("contingency_reversal", 
                                                       "contingency_awareness"), 
                                        na.rm = TRUE)

#plot
ggplot(data = data_3_plot_summary2,
       aes(x = contingency_awareness, 
           y = prob_optimal,
           group = contingency_reversal))+
  geom_point(size = 2,
             aes(color = contingency_reversal),
             position = position_dodge2(.5),)+
  scale_color_manual(values=c("#87b6e8", "#ffbff8"))+
  guides(fill=guide_legend(title="Target Outcome"))+
  geom_errorbar(
    aes(ymin = prob_optimal - se, 
        ymax = prob_optimal + se, 
        color = contingency_reversal),
    width = 0.5,
    position = position_dodge(.5))+
  theme(legend.position=c(0.5, 0.25),
        legend.background = element_rect(fill = "transparent", color = NA))+
  ylim(c(0,1))+
  labs(x = "Contingency awareness",
       y = "Probability of optimal choice",
       color = "Contingency reversal")


#Figure 9C: Reaction time (log) as a function of contingency reversal
data_rt.sum <- data_3_plot%>%
  select(ID_anonymous, optimal, DM_choice_component.rt.log,
         contingency_reversal)%>%
  group_by(ID_anonymous, contingency_reversal)%>%
  dplyr::summarise(mean_RT = mean(DM_choice_component.rt.log, na.rm = TRUE),
                   .groups = "keep")%>%
  ungroup()

data_rt.sum <- as.data.frame(data_rt.sum)
dat.rt.summary <- Rmisc::summarySE(data_rt.sum,
                                   measurevar = "mean_RT",
                                   groupvars = "contingency_reversal",
                                   na.rm = TRUE)

ggplot(dat.rt.summary, aes(x = contingency_reversal, y = mean_RT, 
                           fill = contingency_reversal,
                           ymin = mean_RT - se, 
                           ymax = mean_RT + se)) +
  geom_bar(stat = "identity") +
  geom_errorbar(width = 0.2) +
  labs(x = "Condition", y = "Log of Reaction Time")+
  # Modify the legend colors using scale_color_manual()
  scale_fill_manual(values = custom_colors)+
  theme(legend.position = "none")

