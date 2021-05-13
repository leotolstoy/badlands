import numpy as np 
from demographics import DemographicsModel
from bayesianModel import BayesianModel
from state import State
from populationImporter import Importer
from city import CityModel
from logisticBayesianModel import LogisticBayesianModel

if __name__ == '__main__':
    
    np.random.seed(7000)
    N = 1000
    MAX_YEARS = 100

    # National
    # Educated
    p1 = 'path1'
    p2 = 'path2'
    p3 = 'path3'

	national_edu_turnout_model = LogisticBayesianModel(p2)
	national_edu_voteMargin_model = LogisticBayesianModel(p3)

    #Alaska model paths
    # Educated
    p1 = 'path1'
    p2 = 'path2'
    p3 = 'path3'

    alaska_edu_population_model = LogisticBayesianModel(p1)
	alaska_edu_turnout_model = national_edu_turnout_model
	alaska_edu_voteMargin_model = national_edu_voteMargin_model
	alaska_edu_model = DemographicsModel(alaska_edu_population_model, alaska_edu_turnout_model, alaska_edu_voteMargin_model)

	# non-Educated
    p1 = 'path1'
    p2 = 'path2'
    p3 = 'path3'

    alaska_noedu_population_model = LogisticBayesianModel(p1)
	alaska_noedu_turnout_model = national_noedu_turnout_model
	alaska_noedu_voteMargin_model = national_noedu_voteMargin_model
	alaska_noedu_model = DemographicsModel(alaska_noedu_population_model, alaska_noedu_turnout_model, alaska_noedu_voteMargin_model)

    
    #     Define how many college ed people are coming in , for now a constant amount per year
    population_edu_import = populationModel = ConstantRateModel(50000)
    turnoutModel_import = national_edu_turnout_model
    voteMarginModel_import = national_edu_voteMargin_model
    

    importer_model = Importer(DemographicsModel(population_edu_import, turnoutModel_import, voteMarginModel_import))


    alaska = State(alaska_edu_model, alaska_noedu_model, importer_model)
    
    
    
    for n in range(N):
        #             Generate new time models for state

        fig1, ax1 = plt.subplots(5,1)
    	fig2, ax2 = plt.subplots(5,1)

        alaska.resetState()

        years = []
        population_edu = []
        population_nedu = []
        population_edu_proj = []

        population_projected = []
        population = []


        raw_margin_edu_proj = []
        raw_margin_edu = []
        raw_margin_nedu = []
        raw_margin_proj = []
        raw_margin = []


        
        
        for year in range(MAX_YEARS):
            print(year)
            alaska.evaluateStateAtTime(year)

            years.append(year)
            population_edu_proj.append(alaska.population_edu_proj)
	        population_edu.append(alaska.population_edu)
	        population_nedu.append(alaska.population_nedu)
	        population_proj.append(alaska.population_projected)
	        population.append(alaska.population)


	        raw_margin_edu_proj.append(alaska.raw_margin_edu_proj)
	        raw_margin_edu.append(alaska.raw_margin_edu)
	        raw_margin_nedu.append(alaska.raw_margin_nedu)
	        raw_margin_proj.append(alaska.raw_margin_proj)
	        raw_margin.append(alaska.raw_margin)

            
            if alaska.raw_margin > 0:
                alaska.yearsToFlip.append(year)
                break
                
        
        ax1[0].plot(years,population_edu,'-o',label='population_edu')
        ax1[1].plot(years,population_nedu,'-o',label='population_nedu')
        ax1[2].plot(years,population_edu_proj,'-o',label='population_edu_proj')
        ax1[3].plot(years,population_proj,'-o',label='population_proj')
        ax1[4].plot(years,population,'-o',label='population')
        ax1[-1].set_xlabel('Time (years)')
        ax1.legend()


        ax2[0].plot(years,raw_margin_edu,'-o',label='raw_margin_edu')
        ax2[1].plot(years,raw_margin_nedu,'-o',label='raw_margin_nedu')
        ax2[2].plot(years,raw_margin_edu_proj,'-o',label='raw_margin_edu_proj')
        ax2[3].plot(years,raw_margin_proj,'-o',label='raw_margin_proj')
        ax2[4].plot(years,raw_margin,'-o',label='raw_margin')
        ax2[-1].set_xlabel('Time (years)')
        ax2.legend()
                    
            
    alaska_yearsToFlip = np.array(alaska.yearsToFlip)
    
    plt.figure()
#     plt.subplot(223)
    plt.hist(alaska_yearsToFlip.reshape((-1,)), bins=10)
    plt.title('Alaska years to Flip')
    plt.xlabel("Years to Flip")

	plt.show()
    
    
            
            
        
    
    
