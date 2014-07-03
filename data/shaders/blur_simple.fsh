uniform sampler2D texture0;
uniform sampler2D texture1;
uniform float time;

varying vec2 v_tex;
varying vec2 v_blurTexCoords[14];
varying vec3 v_norm;
varying vec3 v_light;
varying vec3 v_eye;


const float specular_power = 10.0;

void main()
{
    vec4 col = texture2D(texture0,v_tex);
   	float lambert_factor = max(dot(v_norm,v_light),0.);
    float phong_factor   = pow(max(dot(v_norm,normalize(v_light + v_eye)), 0.),specular_power);
    col *= lambert_factor;
    col += phong_factor;
    col.a = 1.0;

    gl_FragColor = col;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[ 0])*0.001;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[ 1])*0.005;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[ 2])*0.01;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[ 3])*0.05;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[ 4])*0.01;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[ 5])*0.02;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[ 6])*0.03;
    gl_FragColor += texture2D(texture0, v_tex         )*0.05;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[ 7])*0.03;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[ 8])*0.02;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[ 9])*0.01;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[10])*0.05;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[11])*0.01;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[12])*0.005;
    gl_FragColor += texture2D(texture0, v_blurTexCoords[13])*0.001;

}
