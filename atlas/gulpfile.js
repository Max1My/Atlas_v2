var gulp = require('gulp'), // main
    sass = require('gulp-sass'), // scss compiler
    sourcemaps = require('gulp-sourcemaps'), // scss sourcemaps
    concat = require('gulp-concat'), // merge two files
    uglify = require('gulp-uglify'), // minify js files
    rename = require('gulp-rename'), // rename files
    cssmin = require('gulp-cssmin'), // minify css files
    merge = require('merge-stream'), // mearge two task
    gulpsequence = require('gulp-sequence'), //  execute multiple task
    babel = require("gulp-babel"), // convert next generation JavaScript, today.
    npmlodash = require("lodash"), // perfoming oops in gulp
    smushit = require('gulp-smushit'), // image optimizer
    autoprefixer = require('gulp-autoprefixer'), // css propertys autoprefixer
    cssbeautify = require('gulp-cssbeautify'), // css cssbeautify
    fileinclude = require('gulp-file-include'), // include html files
    browsersync = require("browser-sync"), // browser reload
    htmlmin = require('gulp-htmlmin'), // html minify
    pgsql = require('gulp-pgsql');


const layout = {
    'layouts': 'vertical', // vertical / horizontal
    'sublayouts': '',
    'darktheme': 'false', // true / false
    'rtltheme': 'false', // true / false
    'bodyclass': '',
    'menuclass': '',
    'headerclass': '',
}

//  [ scss compiler ] start
gulp.task('sass', function() {
    // main style css
    return gulp.src('static/scss/*.scss')
        .pipe(sourcemaps.init())
        .pipe(sass())
        .pipe(autoprefixer())
        .pipe(cssbeautify())
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('static/dist/assets/css'))
})
//  [ scss compiler ] end

//  [ Copy assets ] start
gulp.task('build', function() {
    var required_libs = {
        js: [
            "node_modules/bootstrap/dist/js/bootstrap.min.js",
            "node_modules/perfect-scrollbar/dist/perfect-scrollbar.min.js",
            "node_modules/feather-icons/dist/feather.min.js",
            "node_modules/apexcharts/dist/apexcharts.min.js",
            "node_modules/apexcharts/dist/apexcharts.js"
        ],
        css: [
            "node_modules/bootstrap/dist/css/bootstrap.min.css",
            "node_modules/animate.css/animate.min.css",
        ]
    };
    npmlodash(required_libs).forEach(function(assets, type) {
        if (type == "css") {
            gulp.src(assets)
                .pipe(gulp.dest("static/dist/css/plugins"));
        } else {
            gulp.src(assets)
                .pipe(gulp.dest("static/dist/js/plugins"));
        }
    });
    var cpyassets = gulp.src(['static/assets/**/*.*', '!static/assets/scss/**/*.*'])
        .pipe(gulp.dest('static/dist/assets'));
    return merge(cpyassets);
});

//  [ Copy assets ] end

//  [ build html ] start
gulp.task('build-html', function() {
    return gulp.src('mainapp/templates/mainapp/*.html')
        .pipe(fileinclude({
            context: layout,
            prefix: '@@',
            basepath: '@file',
            indent: true
        }))
        .pipe(gulp.dest('static/dist'))
})
//  [ build html ] end

//  [ build js ] start
gulp.task('build-js', function() {
    var layoutjs = gulp.src('static/assets/js/*.js')
        .pipe(gulp.dest('static/dist/assets/js'))

    var pagesjs = gulp.src('static/js/pages/*.js')
        .pipe(gulp.dest('static/dist/assets/js/pages'))

    return merge(layoutjs, pagesjs);
})
//  [ build js ] end

//  [ scss compiler ] start
gulp.task('mincss', function() {
    // main style css
    return gulp.src('static/scss/*.scss')
        .pipe(sass())
        .pipe(autoprefixer())
        .pipe(cssbeautify())
        .pipe(gulp.dest('static/dist/assets/css'))
        .pipe(cssmin())
        .pipe(gulp.dest('static/dist/assets/css'))
})
//  [ scss compiler ] end

//  [ uglify js ] start
gulp.task('uglify', function() {
    var layoutjs = gulp.src('static/js/*.js')
        .pipe(uglify())
        .pipe(gulp.dest('static/dist/assets/js'))

    var pagesjs = gulp.src('static/js/pages/*.js')
        .pipe(babel())
        .pipe(uglify())
        .pipe(gulp.dest('static/dist/assets/js/pages'))

    return merge(layoutjs, pagesjs);
})
//  [ uglify js ] end

//  [ minify html ] start
gulp.task('htmlmin', function() {
    return gulp.src('mainapp/templates/mainapp/*.html')
        .pipe(fileinclude({
            context: layout,
            prefix: '@@',
            basepath: '@file',
            indent: true
        }))
        .pipe(htmlmin({
            collapseWhitespace: true
        }))
        .pipe(gulp.dest('static/dist'))
})
//  [ minify html ] end

//  [ image optimizer ] start
gulp.task('imgmin', function() {
    return gulp.src('static/img/**/*.{jpg,png}')
        .pipe(smushit())
        .pipe(gulp.dest('static/dist/assets/img'));
});
//  [ image optimizer ] end

//  [ browser reload ] start
gulp.task("browserSync", function() {
    browsersync.init({
        notify: false,
        proxy: "localhost:8000"
    });
});
//  [ browser reload ] end

gulp.task('pgsql', function(done) {
  gulp.src(['db/**/*.pgsql'])
    .pipe(pgsql('psql://postgres@atlas_db/postgres')
      .on('error', pgsql.log)
      .on('notice', pgsql.log)
    )
    .on('finish', done);
});

//  [ watch ] start
gulp.task('watch', function() {
    gulp.watch('static/scss/**/*.scss', gulp.series('sass')).on('change', browsersync.reload);
    gulp.watch('static/js/**/*.js', gulp.series('build-js')).on('change', browsersync.reload);
    gulp.watch('mainapp/templates/mainapp/**/*.html', gulp.series('build-html')).on('change', browsersync.reload);
    gulp.watch('mainapp/templates/mainapp/**/*.html', gulp.series('build')).on('change', browsersync.reload);
    gulp.watch('/var/lib/postgresql/14/main/pg_log/*.log',gulp.series('pgsql')).on('error',pgsql.log).on('notice',browsersync.reload).on('change',browsersync.reload);
})
//  [ watch ] start
const compile = gulp.parallel('browserSync', 'watch');
//  [ Default task ] start
gulp.task('default',
    gulp.series(
        'build',
        'sass',
        'build-js',
        'build-html',
        'imgmin',
        'pgsql',
        compile
    )
);
// gulp.parallel('browserSync','watch')
//  [ Default task ] end

//  [ watch minify ] start
gulp.task('watch-minify', function() {
    gulp.watch('static/scss/**/*.scss', gulp.series('mincss'));
    gulp.watch('static/js/**/*.js', gulp.series('uglify'));
    gulp.watch('mainapp/templates/**/*.html', gulp.series('htmlmin'));
    gulp.watch('mainapp/templates/**/*.html', gulp.series('build'));
})
//  [ watch minify ] start
