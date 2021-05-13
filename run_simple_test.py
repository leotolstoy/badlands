import numpy as np 
from demographics import DemographicsModel
from city import CityModel
from bayesianModel import BayesianModel
from state import State
from populationImporter import Importer


if __name__ == '__main__':
    
    np.random.seed(7000)
    N = 1000
    MAX_YEARS = 100
    
    #Alaska model paths
    p1 = 'path1'
    p2 = 'path2'
    p3 = 'path3'
    
    alaska = State(p1,p2,p3)
    
    #     Define how many college ed people are coming in , for now a constant amount per year
    population_edu_import = 50000
#     Guess some values for the other importer parameters
    turnoutModel_import = 0.6
    regVoterFracModel_import = 0.75
    voteMarginModel_import = 0.2
    

    importer = Importer(population_edu_import, turnoutModel_import, voteMarginModel_import)
    
    fig, ax = plt.subplots()
    
    
    for n in range(N):
        #             Generate new time models for state
        alaska.resampleDemographicsModel('projected')
        importer.resampleDemographicsModel('college_ed')
        years = []
        net_rawVoteMargins = []
        
        
        for year in range(MAX_YEARS):
            print(year)
            alaska.evaluateDemoModelAtTime(year, 'projected')
            
            alaska_voteMargin = alaska.projected_raw_margin
            importer_voteMargin = importer.raw_margin
            
            netRawVoteMargin = alaska_voteMargin + importer_voteMargin
            netRawVoteMargins.append(netRawVoteMargin)
            years.append(year)
            
            
            if netRawVoteMargin > 0:
                alaska.yearsToFlip.append(year)
                break
                
                
        ax.plot(years,netRawVoteMargins,'-o')
        
        
        alaska.resetTimeDemographics('projected')
            
            
    alaska_yearsToFlip = np.array(alaska.yearsToFlip)
    
    
    ax.legend()
    ax.set_ylabel('Vote Margin, Raw (people)')


    ax[-1].set_xlabel('Time (years)')


    
    
    
    plt.figure()
#     plt.subplot(223)
    plt.hist(alaska_yearsToFlip.reshape((-1,)), bins=10)
    plt.title('Alaska years to Flip')
    plt.xlabel("Years to Flip")
    plt.show()
    
    
            
            
        
    
    
    