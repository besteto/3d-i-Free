#version 120
uniform sampler2D texture0;
uniform sampler2D texture1;
uniform float time;

varying vec2 v_tex;
varying vec3 v_light;
varying vec3 v_eye;

const float spec_power = 35.0;
const vec4 spc_light = vec4(0.5,0.5,0.8,1);

void main()
{
    vec4 amb_light = vec4((abs(sin(time))),0,0,1);
    vec4 base_color = texture2D (texture0,v_tex);
	vec4 norm_value = texture2D (texture1,v_tex);

	vec3 normal = 2.0 * norm_value.xyz - 1.0;

	vec3  blinn  = normalize(v_eye + normal);
	float shadow = max(dot(normal, v_light), 0.3);
	float spec   = pow(max(dot(v_light, blinn), 0), spec_power);

    base_color *= shadow * amb_light;
    base_color += spec * spc_light;
	base_color.a = 1.0;
	gl_FragColor = base_color;
}
