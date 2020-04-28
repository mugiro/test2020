APP_CONFIG = {
    'path': '/project/',
    'log_name': 'app',
    'log_file': 'logs/app.log',
    'ALLOWED_EXTENSIONS': ['csv', 'CSV'],
    'meteo_filename': 'meteo.csv',
    'rain_filename': 'rain.csv',
    'gh_units_list': ['wm2', 'jm2'],
    'rain_units_list': ['mm'],
    'time_formats': ['utc', 'solar'],
    'fig_format': '.pdf',
    
    'daily_fig': 'fig_d',
    'daily_dataset': 'df_d',
    'subdaily_fig': 'fig_subd',
    'subdaily_dataset': 'df_subd',
    'subdaily_estimation': 'df_subd_est'
}

# For the docker
APP_CONFIG['dir_data'] = '/mnt/disk/data/'

APP_CONFIG['dir_cis'] = APP_CONFIG['dir_data'] + 'cis/'
APP_CONFIG['dir_dbs'] = APP_CONFIG['dir_data'] + 'dbs/'
APP_CONFIG['dir_out'] = APP_CONFIG['dir_data'] + 'out/'
APP_CONFIG['UPLOAD_FOLDER'] = APP_CONFIG['dir_out']

APP_CONFIG['dir_bulk'] = APP_CONFIG['dir_data'] + 'bulk/'
APP_CONFIG['dir_bk_in'] = APP_CONFIG['dir_bulk'] + 'in/'
APP_CONFIG['dir_bk_out'] = APP_CONFIG['dir_bulk'] + 'out/'
