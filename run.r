library(tidyverse)
r <- read.csv("y.csv")  %>% filter(dist > 4500 & dist < 7000)
p <- ggplot(r,aes(x=dist,y=value,color=type)) +
     geom_smooth(method='loess') +
     scale_x_continuous(sec.axis=sec_axis(trans=(~./1609),
		        name="miles",
                        breaks=seq(0,20,1)),
			name="meters") +
     geom_point() +
     facet_wrap(~type,
                scales = "free_y",
     	        ncol = 2,
		strip.position = "right") +
     scale_color_viridis_d(option = "D") +
     theme_bw()
plot(p)
