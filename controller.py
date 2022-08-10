import interface
import calculator_model
import logger

def data_proces():
    number_operation =0
    while number_operation != 4:
        number_operation = int(interface.inter())
        if number_operation ==1:
            formula = interface.get_value()
            result = calculator_model.calc_int(formula)
            logger.recording_logger(formula, result)
            interface.view(formula, result)
        elif number_operation == 2:
            formula = interface.get_value()
            result = calculator_model.calc_float(formula)
            logger.recording_logger(formula, result)
            interface.view(formula, result)
        elif number_operation ==3:
            logger.output_logger()
        elif number_operation ==4:
            break


