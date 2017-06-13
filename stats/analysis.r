library(nparcomp)

root <- "/Users/aserebrenik/Desktop/Onderzoek/ScratchVars/"
setwd(paste(root,"stats/",sep=""))

#comparing distribution of the variable names' length
icpc2017varlens <- read.csv(paste(root,"sophiko-icpc-2017/extract_variables/result-files/var-len.dat",sep=""),header=TRUE,sep="\t")
scratchvarlens <- read.csv(paste(root,"data_plus_pandas_files/output/distributions\ of\ lengths.csv",sep=""),header=TRUE)

#lbl <- c(rep("PHP",1557390),rep("Java",196545), rep("perl",88754))
#v <- c(rep(5,1305365),rep(6,252025),rep(5,100572),rep(6,95973),rep(5,55774),rep(6,32980))

lbl <- c()
v <- c()
#for (i in c(2:ncol(icpc2017varlens))) { lbl <- c(rep(names(icpc2017varlens)[[i]], sum(icpc2017varlens[[i]])), lbl) }

r <- nrow(icpc2017varlens)
c <- ncol(icpc2017varlens)
for (i in c(1:r)) {
	for (j in c(2:c)) { 
		lbl <- c(rep(names(icpc2017varlens)[[j]], icpc2017varlens[i,j]), lbl)
		v <- c(rep(icpc2017varlens[i,1], icpc2017varlens[i,j]), v)
	}
	cat(".")
}

cat("^")
r <- nrow(scratchvarlens)
for (i in c(1:r)) {
	lbl <- c(rep("scratch", scratchvarlens[i,2]), lbl)
	v <- c(rep(scratchvarlens[i,1], scratchvarlens[i,2]), v)
	cat(".")
}

d <- data.frame(v, lbl)

res <- mctp(d$v~d$lbl, data=d, type="Tukey", asy.method="fisher")

res$Analysis

#               Estimator  Lower  Upper Statistic p.Value
#Java - C           0.190  0.189  0.191   581.035       0
#JS - C            -0.077 -0.077 -0.076  -278.928       0
#perl - C          -0.088 -0.089 -0.087  -226.516       0
#PHP - C            0.122  0.122  0.123   567.042       0
#scratch - C        0.234  0.232  0.235   394.418       0
#JS - Java         -0.267 -0.268 -0.266  -759.737       0
#perl - Java       -0.278 -0.280 -0.277  -618.628       0
#PHP - Java        -0.068 -0.069 -0.067  -224.780       0
#scratch - Java     0.044  0.042  0.045    70.802       0
#perl - JS         -0.012 -0.013 -0.011   -29.672       0
#PHP - JS           0.199  0.198  0.200   769.479       0
#scratch - JS       0.310  0.309  0.312   516.336       0
#PHP - perl         0.211  0.210  0.212   551.758       0
#scratch - perl     0.322  0.320  0.324   476.859       0
#scratch - PHP      0.111  0.110  0.113   192.089       0

# X < Y if Upper < 0 and X > Y if Lower > 0
# The loops below produce two sets of edges for the T-graph
# Copy paste them into digraph.py and generete the T-graph from Python

s_xy <- subset(res$Analysis, Upper < 0)
names <- strsplit(rownames(s_xy), " - ")
for (i in 1:length(names)){
  cat(paste("\"",names[[i]][2],"\" -> ",sep=""), paste("\"",names[[i]][1],"\"",sep=""), "\n")
}

s_yx <- subset(res$Analysis, Lower > 0)
names <- strsplit(rownames(s_yx), " - ")
for (i in 1:length(names)){
  cat(paste("\"",names[[i]][1],"\" -> ",sep=""), paste("\"",names[[i]][2],"\"",sep=""), "\n")
}

#digraph G {
#"C" ->  "JS" 
#"C" ->  "perl" 
#"Java" ->  "JS" 
#"Java" ->  "perl" 
#"Java" ->  "PHP" 
#"JS" ->  "perl" 
#"Java" ->  "C" 
#"PHP" ->  "C" 
#"scratch" ->  "C" 
#"scratch" ->  "Java" 
#"PHP" ->  "JS" 
#"scratch" ->  "JS" 
#"PHP" ->  "perl" 
#"scratch" ->  "perl" 
#"scratch" ->  "PHP" 
#}

#dropping transitive dependencies
#digraph G {
#"C" ->  "JS" 
#"Java" ->  "PHP" 
#"JS" ->  "perl" 
#"PHP" ->  "C" 
#"scratch" ->  "Java" 
#}

icpc2017characters <- read.csv(paste(root,"sophiko-icpc-2017/extract_variables/result-files/char-use.dat",sep=""),header=TRUE)
scratchcharacters <- read.csv(paste(root,"data_plus_pandas_files/output/distributions\ of\ one\ letter\ chars.csv",sep=""),header=TRUE)
scratchaz <- subset(scratchcharacters, grepl("[a-z]",ch))
icpc2017characters$scratch <- scratchaz$count 
nameless <- subset(icpc2017characters, select=-c(ch)) 
row.names(nameless) <- icpc2017characters$ch


forLambdaLower <- t(subset(icpc2017characters, select=c(Clower,JSlower,Javalower,PHPlower,perllower,scratch)))
colnames(forLambdaLower) <- icpc2017characters$ch

library(rapport)
lambda.test(icpc2017characters,1)

library(lsa)
cosine(as.matrix(nameless))
#             Cupper    Clower   JSupper   JSlower Javaupper Javalower  PHPupper  PHPlower perlupper perllower   scratch
#Cupper    1.0000000 0.3611283 0.8412634 0.7173503 0.6803331 0.3109723 0.2205311 0.5245342 0.6528813 0.1794458 0.5935334
#Clower    0.3611283 1.0000000 0.4464655 0.7136214 0.2934833 0.9804554 0.9498817 0.9012264 0.1643316 0.5413309 0.5643843
#JSupper   0.8412634 0.4464655 1.0000000 0.9125161 0.5582298 0.4534770 0.3424506 0.6697455 0.7221644 0.3074593 0.5813263
#JSlower   0.7173503 0.7136214 0.9125161 1.0000000 0.5307265 0.7319082 0.6413899 0.8691923 0.6185908 0.4060138 0.6187956
#Javaupper 0.6803331 0.2934833 0.5582298 0.5307265 1.0000000 0.2605340 0.1741584 0.3622637 0.4050535 0.1806594 0.3928552
#Javalower 0.3109723 0.9804554 0.4534770 0.7319082 0.2605340 1.0000000 0.9761646 0.9206813 0.2097267 0.5616254 0.5933751
#PHPupper  0.2205311 0.9498817 0.3424506 0.6413899 0.1741584 0.9761646 1.0000000 0.8569645 0.1249727 0.5502511 0.5558431
#PHPlower  0.5245342 0.9012264 0.6697455 0.8691923 0.3622637 0.9206813 0.8569645 1.0000000 0.4505609 0.5243181 0.6492839
#perlupper 0.6528813 0.1643316 0.7221644 0.6185908 0.4050535 0.2097267 0.1249727 0.4505609 1.0000000 0.3298945 0.6345022
#perllower 0.1794458 0.5413309 0.3074593 0.4060138 0.1806594 0.5616254 0.5502511 0.5243181 0.3298945 1.0000000 0.3226850
#scratch   0.5935334 0.5643843 0.5813263 0.6187956 0.3928552 0.5933751 0.5558431 0.6492839 0.6345022 0.3226850 1.0000000
#scratch seems to be most similar to PHPlower and perlupper(?), followed by JSlower. 
#in the euclidean world scratch is similar to perlupper
 
nameless_dist <- dist(t(nameless)) #default uses the Euclidean distance
plot(hclust(nameless_dist)) #default complete linkage
# suggests that scratch is similar to the upper cases 
 
plot(hclust(dist(t(nameless), method="euc"), method="ward"))